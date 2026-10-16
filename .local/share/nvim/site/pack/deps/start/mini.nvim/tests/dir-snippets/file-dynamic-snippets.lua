return {
  function(context) return { prefix = 'dyn', body = 'Buf: ' .. context.buf_id, desc = 'Dynamic' } end,
  -- Should also work with function returning (maybe nested) function
  function(_)
    return {
      function(con) return { prefix = 'dynest', body = 'Buf (from nested): ' .. con.buf_id, desc = 'Dynamic nested' } end,
    }
  end,
}
