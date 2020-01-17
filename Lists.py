if __name__ == '__main__':
    N = int(input())
    l =[]

    for _ in range(N):
        input_ = input().split()
        command = input_.pop(0)

        if len(input_) > 0:
            if command == 'insert':
                eval("l.{0}({1}, {2})".format(command, input_[0], input_[1]))
            else:
                eval("l.{0}({1})".format(command, input_[0]))
        elif command == 'print':
            print (l)
        else:
            eval("l.{0}()".format(command))