# PasswordSecurityCheck

The purpose of this project is to check if the input the user provides has ever been leaked as a password.
This is done locally on the machine, in order to not risk compromising the password.

The functional explanation is added in the code as comments.

The main idea is that the user gives a password that has to be compared to a database of leaked passwords.
This is done by using the API of the page https://api.pwnedpasswords.com/range/ that returns a list of parts of hashes and a leak-counter corresponding to our password.

If our password was found, the number of leaks will be displayed.

The code can be run as is via an IDE, or slightly adapted to be run via the terminal with arguments.
Or it also contains instructions to create an exe file.


On a side note:

At the time of writing, the password "123456" was found 24230577 times as leaked password, which is laughable considering that password managers exist.
I personally am a fan of https://keepass.info/ which is a 'free, open source, light-weight and easy-to-use password manager'. I simply love it.

Best,
Steve
