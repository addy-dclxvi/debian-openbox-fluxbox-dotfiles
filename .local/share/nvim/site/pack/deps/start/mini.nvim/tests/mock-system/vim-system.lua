-- Queue of what `vim.system` should return as its `SystemObjCompleted`.
-- Each call takes first entry and uses it. Entries can be:
-- - Partial `SystemObjCompleted`, others inferred with custom defaults.
--   Both `stdout` and `stderr` can be array of lines (instead of 'aa\nbb').
-- - `{ delay: integer, sys_out: SystemObjCompleted }` - more elaborate way
--   to control the delay of each one.
_G.system_queue = {}

-- - `:h SystemObjCompleted`
_G.sys_out_default = { code = 0, signal = 0, stdout = '', stderr = '' }
_G.sys_out_terminated = { code = 0, signal = 0, stdout = '', stderr = '' }
_G.delay_default = 0

-- Log of how `vim.system()` is used
_G.system_log = {}

vim.system = function(cmd, opts, on_exit)
  local data = _G.system_queue[1]
  if data == nil then error('Can not mock `vim.system`: `_G.system_output_queue[1]` is nil') end
  table.remove(_G.system_queue, 1)

  table.insert(_G.system_log, { 'vim.system', { cmd = cmd, opts = opts } })

  -- Prepare output object
  if data.sys_out == nil then data = { sys_out = data } end
  data = vim.tbl_deep_extend('force', { delay = _G.delay_default, sys_out = _G.sys_out_default }, data)
  local stdout = data.sys_out.stdout
  data.sys_out.stdout = type(stdout) == 'table' and table.concat(stdout, '\n') or stdout

  -- Schedule CLI exit
  local has_exited = false
  vim.defer_fn(function()
    has_exited = true
    if vim.is_callable(on_exit) then on_exit(data.sys_out) end
  end, data.delay)

  -- `:h SystemObj`
  local res = {}
  res.is_closing = function(_)
    table.insert(_G.system_log, { 'is_closing' })
    return has_exited
  end
  res.kill = function(_, ...) table.insert(_G.system_log, { 'kill', { ... } }) end
  res.wait = function(_, timeout)
    table.insert(_G.system_log, { 'wait', { timeout } })

    vim.wait(timeout or 10000000, function() return has_exited end)
    if has_exited then return data.sys_out end
    res:kill(9)
    return { code = 124, signal = 9, stdout = '', stderr = '' }
  end
  res.write = function(_, ...) table.insert(_G.system_log, { 'write', { ... } }) end

  return res
end
