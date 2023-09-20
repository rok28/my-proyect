def main():
    palabra = input("Introduce la palabra: ")
    palindromo = palabra == palabra[::-1]
    if palindromo:
        rest = "La palabra " + palabra + " es palindromo"
    else:
        rest = "La palabra " + palabra + " no es palindromo"
    print(rest)
main()
