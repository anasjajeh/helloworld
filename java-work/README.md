instructions to compile and run a single java class in terminal:

1. create a folder and put the `<MY_CLASS>.java` file and a `manifest.txt` file in it. The `manifest.txt` file should contain the following line: `Main-Class: <MY_CLASS>`

1. compile the source file with `javac -d . *.java`

1. make the java app (`.jar` file) with `jar cvfm <APP_NAME>.jar manifest.txt <MY_CLASS>.class` You can rename it, and put it wherever you want.

1. run the app with `java -jar <APP_NAME>.jar`
