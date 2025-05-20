

class Command:
    def execute(self):
        pass
    def undo(self):
        pass
    
class TextEditor:
    def __init__(self):
        self.text = ""
    def write(self,text):
        self.text += text
        
    def delete(self,count):
        self.text = self.text[:count]
        
    def show(self):
        print(self.text)
        

class WriteCommand(Command):
    def __init__(self,editor,text):
        self.editor = editor
        self.text = text
        
    def execute(self):
        self.editor.write(self.text)
        
    def undo(self):
        self.editor.delete(len(self.text))
        


class CommandManager:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []
        
    def execute_command(self, command):
        command.execute()
        self._undo_stack.append(command)
        self._redo_stack.clear()
        
    def undo(self):
        if self._undo_stack:
            cmd = self._undo_stack.pop()
            cmd.undo()
            self._redo_stack.append(cmd)
        else:
            print("Nothing to undo.")
    
    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack.pop()
            cmd.execute()
            self._undo_stack.append(cmd)
        else:
            print("Nothing to redo.")

            
            
editor = TextEditor()
manager = CommandManager()

# Write some text
manager.execute_command(WriteCommand(editor, "Hello "))
manager.execute_command(WriteCommand(editor, "World!"))
editor.show()  # Hello World!

# Undo last action
manager.undo()
editor.show()  # Hello

# Redo last action
manager.redo()
editor.show()  # Hello World!

        