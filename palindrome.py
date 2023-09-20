def main():
    palabra = input("Introduce la palabra: ")
    w_palabra = palabra.replace(" ","")
    palindromo = w_palabra == w_palabra[::-1]
    if palindromo:
        rest = "La palabra " + palabra + " es palindromo"
    else:
        rest = "La palabra " + palabra + " no es palindromo"
    print(rest)
main()
