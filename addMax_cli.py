import argparse

def calc(args):
    if args.n == 1:
        return f"The sum of given numbers is {sum(args.list)}\n"
    else:
        return f"The largest number is {max(args.list)}\n"



def cli(l,n):
    parser = argparse.ArgumentParser(
        description="Addition of numbers and finding largest of given numbers"
    )
    parser.add_argument(
        "list", metavar="numbers", nargs="*", type=int, help="Eneter list of numbers"
    )
    parser.add_argument(
        "--n", metavar="n",type=int, default=1, help="Enter 2 to print largest number"
    )
    t=["--n",str(n)]
    l=t+l
    args = parser.parse_args(l)
    print(str(calc(args)))


if __name__ == "__main__":
    print("""             
             *********************** ADD-MAX CLI ******************************
             *   Enter a list of numbers and select any one of the following: *
             *   1. Print sum of given numbers                                *
             *   2. Print the largest number in given list                    *
             *   3. Exit                                                      *
             ******************************************************************\n""")
    l=input("Enter list of numbers:").split()
    n=input("Enter your choice:")
    while(n not in ['1','2','3']):
        n=input("Enter a valid choice:")
    if(n!='3'):
        cli(l,n)
    else:
        print("Thank you for using ADD-MAX CLI")
