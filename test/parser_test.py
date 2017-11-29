from monkey.parser import Parser


class TestParser:

    def test_let_statements(self):
        input = '''
            let x = 5;
            let y = 10;
            let foobar = 838383;
        '''

        parser = Parser(input)

        program = parser.parse_program()

        assert program is not None
        assert len(program.statements) == 3
