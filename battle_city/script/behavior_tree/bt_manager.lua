
require "behavior_tree.behavior_node"
require "behavior_tree.behavior_tree"

local json = require "cjson"

local M = {}
-- 导出节点说明配置
function M.export_node_doc()
  local data = "["
  for name, c in pairs(_G) do
    if type(c) == "table" and c.super == BehaviorNode then
      local obj = c.new()
      local doc = obj.doc
      if doc then
        doc.name = name
        data = data .. json.encode(doc) .. ",\n" 
      end
    end
  end

  if data ~= "[" then
    data = string.sub(data, 1,-3)
    data = data .. "]"
  end

  local file = io.open(WORKSPACE.."data/btree/node_doc.txt", "w")
  file:write(data)
end

local id2tree_data = {}
function M.load_trees()
  local dir = WORKSPACE.."data/btree/tree/"
  local s = io.popen("ls ".. dir)
  local fileLists = s:read("*all")
  while true do
    _,end_pos, filename = string.find(fileLists, "([^\n\r]+.txt)", start_pos)
    if not end_pos then 
      break
    end
    local file = io.open(dir..filename, "r")
    local str = file:read()
    local data = json.decode(str)
    id2tree_data[data.tree_id] = data
    start_pos = end_pos + 1
  end

end

function M.create_tree(tree_id, owner)
  local tree_data = id2tree_data[tree_id]
  if not tree_data then
    print("behavior tree not exist, tree_id:"..tree_id)
    return
  end
  return BehaviorTree.new(tree_data, owner)
end

return M