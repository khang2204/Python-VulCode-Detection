def manageModelStatus(entity_logic, status_retriever=None):...
"""docstring"""
def manageModelsStatus(request, *args, **kwargs):...
"""docstring"""
post_dict = request.POST
new_status = post_dict.get('new_status')
if not new_status:
if not status_retriever or not callable(status_retriever):
if not 'fields' in post_dict:
return error_handler.logErrorAndReturnOK(
    'No valid status can be set by the manageModelStatus.')
error_handler.logErrorAndReturnOK(
    'No fields to filter on found for manageModelStatus.')
fields = pickle.loads(str(post_dict['fields']))
entities = entity_logic.getForFields(fields, limit=BATCH_SIZE)
for entity in entities:
if new_status:
db.put(entities)
status = new_status
status = status_retriever(entity)
if len(entities) == BATCH_SIZE:
entity.status = status
context = post_dict.copy()
return responses.terminateTask()
return responses.startTask(request.path, context=context)
