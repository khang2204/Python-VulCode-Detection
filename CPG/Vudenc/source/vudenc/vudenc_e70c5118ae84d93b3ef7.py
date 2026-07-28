def test_add_command(self):...
sievelib.commands.add_commands(MytestCommand)
sievelib.commands.get_command_instance('mytest')
self.assertRaises(sievelib.commands.UnknownCommand, sievelib.commands.
    get_command_instance, 'unknowncommand')
self.compilation_ok(
    """
        mytest :testtag 10 ["testrecp1@example.com"];
        """)
