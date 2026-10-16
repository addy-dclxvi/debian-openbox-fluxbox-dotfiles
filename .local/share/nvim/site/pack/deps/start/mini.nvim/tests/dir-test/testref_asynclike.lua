local T = MiniTest.new_set()

T['async-like'] = function()
  -- Although this is synchronous, it is very async-like as it forces scheduled
  -- functions to be executed while it waits for its condition.
  -- Thiscan interfere with how test step execution is done, as each of them
  -- is scheduled.
  vim.wait(_G.wait_time, function() return false end, 0.25 * _G.wait_time)
  MiniTest.expect.equality(false, true)
end

return T
