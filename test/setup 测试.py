

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# 使用for循环,每次读一行
# for line in open('01_test.txt'):
#     print(line)


# 使用for循环,每次读一行,去空格版
# for line in open('01_test.txt'):
#     print(line.strip())

# 生成器方法
# lineiter = (line.strip() for line in open('01_test.txt'))
# for line in lineiter:
#     print(line)

# 读取内容,每一行作为列表中的一个元素,不要已 # 开头
# lineiter = (line.strip() for line in open('01_test.txt'))
# list = [line for line in lineiter if line and not line.startswith("#")]
# print(list)


from os.path import join, dirname

# with open(join(dirname(__file__), './VERSION.txt'), 'rb') as f:
#     version = f.read().decode('ascii').strip()
print(dirname(__file__))  # 获取当前文件的目录
print(join(dirname(__file__),'./VERSION.txt'))  # 获取'./VERSION.txt'的目录