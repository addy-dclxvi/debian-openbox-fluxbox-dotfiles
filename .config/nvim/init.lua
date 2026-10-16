vim.g.mapleader = ' '
vim.g.maplocalleader = '\\'

-- Bootstrap mini.nvim, the one and only installed plugin, then load its modules
local path_package = vim.fn.stdpath('data') .. '/site/'
local mini_path = path_package .. 'pack/deps/start/mini.nvim'
if not vim.loop.fs_stat(mini_path) then
	vim.cmd('echo "Installing `mini.nvim`..." | redraw')
	vim.fn.system({
		'git', 'clone', '--filter=blob:none',
		'--branch', 'stable',
		'https://github.com/nvim-mini/mini.nvim', mini_path
	})
end
require('mini.deps').setup({ path = { package = path_package } })

local miniclue = require('mini.clue')
miniclue.setup({
	triggers = {
		{ mode = 'c', keys = '<C-r>' },
		{ mode = 'i', keys = '<C-r>' }, { mode = 'i', keys = '<C-x>' },
		{ mode = 'n', keys = "'" }, { mode = 'n', keys = '"' },
		{ mode = 'n', keys = '<C-w>' }, { mode = 'n', keys = '<Leader>' },
		{ mode = 'n', keys = '[' }, { mode = 'n', keys = ']' }, { mode = 'n', keys = '`' },
		{ mode = 'n', keys = 'g' }, { mode = 'n', keys = 'z' },
		{ mode = 'x', keys = "'" }, { mode = 'x', keys = '"' },
		{ mode = 'x', keys = '<Leader>' }, { mode = 'x', keys = '`' },
		{ mode = 'x', keys = 'g' }, { mode = 'x', keys = 'z' },
	},
	clues = {
		miniclue.gen_clues.builtin_completion(), miniclue.gen_clues.g(),
		miniclue.gen_clues.marks(), miniclue.gen_clues.registers(),
		miniclue.gen_clues.windows(), miniclue.gen_clues.z(),
	},
	window = { delay = 200}
})

local hipatterns = require('mini.hipatterns')
hipatterns.setup({
	highlighters = { hex_color = hipatterns.gen_highlighter.hex_color() }
})

require('mini.basics').setup({
	options = { basic = true, extra_ui = true },
	mappings = { basic = true, windows = true },
	autocommands = { basic = true, relnum_in_visual_mode = true }
})

require('mini.completion').setup({
	lsp_completion = { auto_setup = false },
	fallback_action = function()
		local line = vim.api.nvim_get_current_line()
		local col = vim.api.nvim_win_get_cursor(0)[2]
		local word = line:sub(1, col):match("%S+$") or ""
		local keys = (word:match("/") or word:match("%.%.?")) and "<C-x><C-f>" or "<C-x><C-n>"
		vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes(keys, true, true, true), "n", true)
	end
})

pcall(vim.cmd, 'colorscheme miniwinter')
vim.opt.background = 'light'
require('mini.colors').setup()
require('mini.hues').setup({
	background = '#efefef',
	foreground = '#575757',
	saturation = 'high'
})

require('mini.statusline').setup({
	vim.api.nvim_set_hl(0, 'Empty', { bg = NONE, fg = NONE }),
	use_icons = false,
	content = {
		active = function()
			local mode, mode_hl = MiniStatusline.section_mode({ trunc_width = 80, icon = '' })
			local filename = MiniStatusline.section_filename({ trunc_width = 240, icon = '' })
			return MiniStatusline.combine_groups({
				{ hl = mode_hl, strings = { mode } },
				{ hl = 'Empty', strings = { '' } }, '%<',
				{ hl = 'Empty', strings = { '' } }, '%=',
				{ hl = 'Empty', strings = { '' } },
				{ hl = 'MiniStatuslineFileinfo', strings = { filename } }
			})
		end,
		inactive = function()
			local filename = MiniStatusline.section_filename({ trunc_width = 240, icon = '' })
			return MiniStatusline.combine_groups({
				{ hl = 'Empty', strings = { '' } }, '%<',
				{ hl = 'Empty', strings = { '' } }, '%=',
				{ hl = 'Empty', strings = { '' } },
				{ hl = 'MiniStatuslineFileinfo', strings = { filename } }
			})
		end
	}
})

require('mini.icons').setup({ style = 'ascii' })
require('mini.starter').setup({ header = '' })
require('mini.tabline').setup({ show_icons = false })

require('mini.ai').setup()
require('mini.align').setup()
require('mini.animate').setup()
require('mini.bracketed').setup()
require('mini.bufremove').setup()
require('mini.cmdline').setup()
require('mini.comment').setup()
require('mini.cursorword').setup()
require('mini.extra').setup()
require('mini.files').setup()
require('mini.fuzzy').setup()
require('mini.indentscope').setup()
require('mini.input').setup()
require('mini.jump').setup()
require('mini.jump2d').setup()
require('mini.map').setup()
require('mini.misc').setup()
require('mini.move').setup()
require('mini.notify').setup()
require('mini.operators').setup()
require('mini.pairs').setup()
require('mini.pick').setup()
require('mini.sessions').setup()
require('mini.splitjoin').setup()
require('mini.surround').setup()
require('mini.trailspace').setup()
require('mini.visits').setup()

-- require('mini.base16').setup()
-- require('mini.diff').setup()
-- require('mini.doc').setup()
-- require('mini.git').setup()
-- require('mini.keymap').setup()
-- require('mini.snippets').setup()
-- require('mini.test').setup()

-- Shortcuts
local map = vim.keymap.set
map('n', '<Leader>c', 'gcc', { remap = true, desc = 'Comment toggle' })
map('n', '<Leader>q', '<Cmd>quit<CR>', { desc = 'Quit' })
map('n', '<Leader>Q', '<Cmd>quit!<CR>', { desc = 'Quit without saving' })
map('n', '<Leader>w', '<Cmd>update<CR>', { desc = 'Write change' })
map('n', '<Leader>W', '<Cmd>wq<CR>', { desc = 'Write change and exit' })
map('n', '<Leader>/', function() vim.cmd('nohlsearch') end, { desc = 'Clear search highlight' })
map('n', '<Leader>b', function() require('mini.pick').builtin.buffers() end, { desc = 'Buffers' })
map('n', '<Leader>d', function() require('mini.sessions').delete('default', { force = true }); print('Session deleted!') end, { desc = 'Delete session' })
map('n', '<Leader>f', function() require('mini.files').open() end, { desc = 'File Explorer' })
map('n', '<Leader>l', function() require('mini.sessions').read('default') end, { desc = 'Load session' })
map('n', '<Leader>m', function() require('mini.map').toggle() end, { desc = 'Mini Map' })
map('n', '<Leader>n', function() vim.wo.number = not vim.wo.number; vim.wo.signcolumn = vim.wo.number and 'yes' or 'no' end, { desc = 'Toggle Number' })
map('n', '<Leader>p', function() require('mini.pick').builtin.files() end, { desc = 'Pick Files' })
map('n', '<Leader>r', function() vim.cmd('source $MYVIMRC') print('Config reloaded!') end, { desc = 'Reload Config' })
map('n', '<Leader>s', function() require('mini.sessions').write('default'); print('Session saved!') end, { desc = 'Save session' })
map('n', '<Leader>t', function() require('mini.trailspace').trim() end, { desc = 'Trim Trailspace' })
map('n', '<Leader>v', function() require('mini.visits').select_path() end, { desc = 'Visit Paths' })
map('n', '<Leader>z', function() require('mini.misc').zoom() end, { desc = 'Zoom Window' })
vim.keymap.set({'n', 'i', 'v'}, '<C-/>', '<Cmd>nohlsearch<CR>', { desc = 'Clear highlight' })
vim.keymap.set({'n', 'i', 'v'}, '<C-z>', '<Cmd>undo<CR>', { desc = 'Undo' })
vim.keymap.set('i', '<C-BS>', '<C-W>', { noremap = true, silent = true, desc = 'Delete word' })

-- Overriding some of mini.basics settings
vim.opt.list = true -- Make invisible characters visible
vim.opt.mouse = "" -- Disable mouse
vim.opt.scrolloff = 8 -- To see what is coming next
vim.opt.shiftwidth = 4 -- The default 8 spaces is too deep
vim.opt.showtabline = 1 -- Only shows window tab when there are more than one
vim.opt.tabstop = 4 -- The default 8 spaces is too deep
MiniIcons.mock_nvim_web_devicons()
MiniMisc.setup_restore_cursor()
