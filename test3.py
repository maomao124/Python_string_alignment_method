"""
 * Project name(项目名称)：Python字符串对齐方法
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:15
 * Version(版本): 1.0
 * Description(描述)： Python center()方法
center() 字符串方法与 ljust() 和 rjust() 的用法类似，但它让文本居中，而不是左对齐或右对齐。
S.center(width[, fillchar])
 """

if __name__ == '__main__':
    str1 = "1234567890"
    print(str1.center(30))
    print(str1.center(30, "-"))
    print(str1.center(30, "*"))
    print(str1.center(30, "0"))
    print(str1.center(30, "\b"))
    print(str1.center(30, "\t"))
    print(str1.center(30, "\n"))

    input()
