import sys
import cookie

def main():
	if  argv[2] != '-d' or len(argv) < 4:
        print("Arguments not correct. Please use the format below.")
        print("\t./most_active_cookie [csv file] -d [date]")
        sys.exit()

    #read args
    file, option, arg = sys.argv[1:]
    cookie = src.cookie()
    cookie.read_log(file)

    #print results
    results = cookie.get_freq(arg)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()