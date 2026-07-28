def delete_app(self):...
"""docstring"""
contract = jc.Contract()
return st.OperationContract(self.agent.make_delete_app_operation(bindings=
    self.bindings, application=self.TEST_APP), contract=contract)
