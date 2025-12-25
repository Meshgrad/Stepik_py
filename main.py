


def sand_clock():
    def st(num, step):
        print(f'{str(step) * num}'.center(16))
        if step < 4:
            st(num - 4, step + 1)
            print(f'{str(step) * num}'.center(16))  
    st(16, 1)
sand_clock()