"""
 * Project name(项目名称)：Python字符串对齐方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:07
 * Version(版本): 1.0
 * Description(描述)： Python ljust()方法
ljust() 方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。
ljust() 方法
S.ljust(width[, fillchar])
其中:
S：表示要进行填充的字符串；
width：表示包括 S 本身长度在内，字符串要占的总长度；
fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。
 """

if __name__ == '__main__':
    str1 = "1234567890"
    print(str1.ljust(30))
    print(str1.ljust(30, "-"))
    print(str1.ljust(30, "*"))
    print(str1.ljust(30, "0"))
    print(str1.ljust(30, "\b"))
    print(str1.ljust(30, "\t"))
    print(str1.ljust(30, "\n"))

    input()


