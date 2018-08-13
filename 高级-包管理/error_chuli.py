'''
异常：
        广义上的错误分为错误和异常
        错误指的是可以认为避免
        异常是指在语法逻辑正确的前提下，出现的问题
        在python里，异常是一个类，可以处理和使用
    异常处理：
        不能保证程序永远正确运行
        但是，必须保证程序在最坏的情况下得到的问题被妥善处理
        python的一次处理模块全部语法为：
            try:
                尝试实现某个操作
                如果没出现异常，任务就可以完成
                如果出现异常，讲异常从当前代码块扔出去尝试解决异常
            except 异常类型1：
                解决方案1：用于尝试在此处异常解决问题
            except 异常类型2：
                解决方案2：用于尝试在此处异常解决问题
            except （异常类型1，异常处理2......）：
                解决方案:针对多个异常使用相同的处理方式
            except:
                解决方案：所有异常的解决方案
            else:
                如果没有出现任何异常，将会执行此处代码
            finally:
                管你有没有异常都要执行的代码
        流程：
            1、执行try下面的语句
            2、如果出现异常，则在except语句查找对应异常并进行处理
            3、如果没有出现异常，则执行else语句内容
            4、最后，不管是否出现异常，都要执行finally语句
            除except(最少一个）以外，else和finally可选
                    如果是多种error的情况，需要把越具体的错误越往前放
                    在异常类继承关系中，越是子类的异常，越要往前放
                    越是父类的异常，越要往后放
                    在处理异常的时候，一旦拦截到某一个异常，则不再继续往下查看，直接进行下一个代码
                    即有finally则执行finally语句块，否则就执行下一个大的语句
                    所有异常都是继承自Exception
                    如果写上下面这句话，任何异常都会拦截住
                    而且，下面这句话一定是最后一个exception
                        except Exception as e:
                            print('我也不知道就出错了')
                            print(e)
    用户手动引发异常
        当某些情况，用户希望自己引发一个异常的时候，可以使用
        raise 关键字来引发异常
            #raise案例-1
            try:
                print('woailiangzhoumei')
                print(3.1415926)
                #手动引发一个异常
                # 注意语法：raise ErrorClassName
                raise ValueError
                print('还没完呀')
            except NameError as e:
                print('NameError')
            except ValueError as e:
                print('ValueError')
            except Exception as e:
                print('有异常')
            finally:
                print('我肯定会被执行的')

             #raise案例-2
             #自己定义异常
             #需要注意：自定义异常必须是系统异常的子类
             class DanaValueError(ValueError):
                pass
            try:
                print('woailiangzhoumei')
                print(3.1415926)
                #手动引发一个异常
                # 注意语法：raise ErrorClassName
                raise DnaValueError
                print('还没完呀')
            except NameError as e:
                print('NameError')
            except ValueError as e:
                print('ValueError')
            except Exception as e:
                print('有异常')
            finally:
                print('我肯定会被执行的')
    关于自定义异常:
            只要是raise异常，则推荐自定义异常
            在自定义异常的时候，一般包含以下内容：
                自定义发生异常的异常代码
                自定义发生异常后的问题提示
                自定义发生异常的行数
            最终目的是，一旦发生异常，方便程序员快速定位错误现场


'''