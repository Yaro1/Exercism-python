students_default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                    'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
name_flowers = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}


class Garden:
    def __init__(self, diagram, students=students_default):
        diagram = ''.join(diagram.split('\n'))
        step = len(diagram) // 2
        self.dictionary = dict(
                [
                 (x, [name_flowers[y] for y in diagram[num*2:num*2+2] + diagram[num*2+step:num*2+step+2]])
                 for x, num in zip(sorted(students), range(len(students)))
                ]
            )

    def plants(self, name):
        return self.dictionary[name]