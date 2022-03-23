"""
 * Project name(项目名称)：Python字符串对齐方法
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:13
 * Version(版本): 1.0
 * Description(描述)： Python rjust()方法
rjust() 和 ljust() 方法类似，唯一的不同在于，rjust() 方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。
rjust() 方法
S.rjust(width[, fillchar])
 """

if __name__ == '__main__':
    str1 = "1234567890"
    print(str1.rjust(30))
    print(str1.rjust(30, "-"))
    print(str1.rjust(30, "*"))
    print(str1.rjust(30, "0"))
    print(str1.rjust(30, "\b"))
    print(str1.rjust(30, "\t"))
    print(str1.rjust(30, "\n"))

    input()
