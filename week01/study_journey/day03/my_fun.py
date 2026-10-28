__all__ = ['circle_len','circle_area']
PI = 3.1415926
def circle_area(r):
    area = round(PI * r ** 2,2)
    return area

def circle_len(r):
    len = round(2 * PI *r,2)
    return len

if __name__ == '__main__':
    print(circle_area(10))