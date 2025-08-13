def KEY(**kwrgs):
    print(kwrgs)
    print(type(kwrgs))
    for key, value in kwrgs.items():
        print(f"{key}: {value}")

KEY(name = "Sachdev", Age = 22, Institution = "UIET", Ocupation = 'Student')