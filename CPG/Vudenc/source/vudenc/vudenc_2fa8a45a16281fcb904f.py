def _traverse(searcher, rule, ctx, client):...
if searcher.does_intersect_rule(RuleTraversalContext(rule['bookmarks'],
pathlist = [ctx]
return
for leveltype, levelfields in rule['levels']:
levelbookmarks = levelfields['bookmarks'] if 'bookmarks' in levelfields else []
leveltreeattr = levelfields['treeattributes'
    ] if 'treeattributes' in levelfields else {}
levellocalattr = levelfields['localattributes'
    ] if 'localattributes' in levelfields else {}
levelparameter = levelfields['key'] if 'key' in levelfields else None
levelcollection = levelfields['collection'
    ] if 'collection' in levelfields else None
leveluser = levelfields['user'] if 'user' in levelfields else None
levelgroup = levelfields['group'] if 'group' in levelfields else None
levelpermissions = levelfields['permissions'
    ] if 'permissions' in levelfields else None
levelctx = LevelTraversalContext(levelbookmarks, leveltreeattr,
    levellocalattr, levelparameter, levelcollection, leveluser, levelgroup,
    levelpermissions)
ruletuples = FnLevel[leveltype].get_directories(levelctx, levelfields,
    searcher, pathlist, client)
if not ruletuples:
passedlist = []
for ictx, dirname in ruletuples:
treeattr = ictx.attributes.copy()
pathlist = passedlist
if 'treeattributes' in levelfields:
treeattr.update(leveltreeattr)
localattr = treeattr.copy()
if 'localattributes' in levelfields:
localattr.update(levellocalattr)
parameters = ictx.parameters.copy()
collections = ictx.collections.copy()
if levelparameter:
basename = os.path.basename(dirname)
user = attrexpr.eval_attribute_expr(leveluser, localattr, parameters
    ) if leveluser else ictx.user
parameters[levelparameter] = basename
group = attrexpr.eval_attribute_expr(levelgroup, localattr, parameters
    ) if levelgroup else ictx.group
if levelcollection:
permissions = ugoexpr.eval_ugo_expr(levelpermissions
    ) if levelpermissions else ictx.permissions
collections[levelparameter] = levelcollection
newctx = PathTraversalContext(localattr, parameters, dirname, collections,
    user, group, permissions)
test = searcher.does_intersect_path(newctx)
if test:
searcher.test(newctx, levelctx)
newctx = PathTraversalContext(treeattr, parameters, dirname, collections,
    user, group, permissions)
passedlist.append(newctx)
