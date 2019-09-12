# coding=gbk
import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

class Person:
    _num = 0

    def __init__(self, name, gender, birthday, ident):
        # 对姓名和性别进行检查
        if not isinstance(name, str) and gender in ("女", "男"):
            raise PersonValueError(name, gender)

        try:
            # * 接受任意多个参数并放在同一个元组中
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)

        self._name = name
        self._gender = gender
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def gender(self):
        return self._gender

    def birthday(self):
        return self._birthday

    def age(self):
        # 标准库date类的today方法返回函数调用时刻的日期，是一个date对象
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name =name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._id, self._name, self._gender, str(self._birthday)))

    def details(self):
        return ", ".join(("编号： "+self._id,
                          "姓名： "+self._name,
                          "性别： "+self._gender,
                          "出生日期: "+str(self._birthday)))

class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, gender, birthday, department):
        Person.__init__(self, name, gender, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected", course_name)
        self._courses[course_name] = score



p1 = Person("谢雨洁", "女", (1995, 7, 30), "1201510111")
p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
p3 = Person("张子玉", "女", (1974, 10, 16), "0197401032")
p4 = Person("李国栋", "男", (1962, 5, 24), "0196212018")

plist2 = [p1, p2, p3, p4]
for p in plist2:
    print(p)

print("\nAfter sorting:")
plist2.sort()
for p in plist2:
    print(p.details())

print("People created:", Person.num(), "\n")