from cmath import pi
import math

#######################################################
##     Funções para o Prisma Triangular Regular      ##
#######################################################


def areaBaseSemAltura(lado):
    areaBase = ((lado ** 2) * math.sqrt(3))/4
    print('A área da base é: %.2f\n' % areaBase)


def areaBaseComAltura(base, altura):
    areaBase = (base * altura)/2
    print('A área da base é: %.2f\n' % areaBase)


def areaLateral(lado, altura):
    areaLateral = lado * altura
    print('O valor da área de uma lateral é: %.2f\n' % areaLateral)


def areaTotalLateral(lado, altura):
    areaLateral = lado * altura
    areaTotal = areaLateral * 3
    print('Área lateral do prisma: %.2f' % areaLateral)
    print('Área total das laterais: %.2f\n' % areaTotal)


def areaTotalPrisma1(lado, altura):
    areaBase = ((lado ** 2) * math.sqrt(3))/4
    areaLateral = lado * altura
    areaTotal = (areaBase * 2) + (areaLateral * 3)
    print('Área total do prisma: %.2f\n' % areaTotal)


def areaTotalPrisma2(base, alturatriangulo, altura):
    areaBase = (base * alturatriangulo)/2
    areaLateral = base * altura
    areaTotal = (areaBase * 2) + (areaLateral * 3)
    print('Área total do prisma: %.2f\n' % areaTotal)


def areaTotalComBases(areaBase, areaLateral):
    areaTotal = (2 * areaBase) + (3 * areaLateral)
    print('A área total é: %.2f\n' % areaTotal)


def volumeComArea(areaBase, altura):
    volumePrisma = areaBase * altura
    print('Volume do prisma triângular: %.2f\n' % volumePrisma)


def volumeSemArea(lado, altura):
    areaBase = ((lado ** 2) * math.sqrt(3))/4
    volumePrisma = areaBase * altura
    print('Volume do prisma triângular: %.2f\n' % volumePrisma)


#######################################################
##     Funções para o Prisma Hexagonal Regular       ##
#######################################################


def areaBaseHex(lado):
    areaBase = ((3 * (lado ** 2)) * (math.sqrt(3)))/2
    print('Área da base: %.2f\n' % areaBase)


def areaLateralHex(lado, altura):
    areaLateral = lado * altura
    print('Área lateral: %.2f\n' % areaLateral)


def areaTotalLateralex(lado, altura):
    areaLateral = lado * altura
    print('Área lateral: %.2f' % areaLateral)
    areaTotal = areaLateral * 6
    print('Área total das laterais: %.2f\n' % areaTotal)


def areaTotalComAreasHex(areaBase, areaLateral):
    areaTotal = (areaBase * 2) + (areaLateral * 6)
    print('Área total do prisma: %.2f\n' % areaTotal)


def areaTotalComMedidasHex(lado, altura):
    areaBase = ((3 * (lado ** 2)) * (math.sqrt(3)))/2
    areaLateral = lado * altura
    areaTotal = (areaBase * 2) + (areaLateral * 6)
    print('Área total do prisma: %.2f\n' % areaTotal)


def volumePrismaHex(areaBase, altura):
    volumePrisma = areaBase * altura
    print('Volume do prisma: %.2f\n' % volumePrisma)


def volumePrismaComMedidas(lado, altura):
    areaBase = ((3 * (lado ** 2)) * (math.sqrt(3)))/2
    volumePrisma = areaBase * altura
    print('Volume do prisma: %.2f\n' % volumePrisma)


#######################################################
##                   Calculadora                     ##
#######################################################

laco = True
while laco:
    print('||||       Calculadora: Prisma Triângular Regular      ||||')
    print('||||             e Prisma Hexagonal Regular            ||||')
    print('||||        Informe a opção desejada para calculo:     ||||')
    print('||||      1 - Área da base do prisma triângular        ||||')
    print('||||      2 - Área lateral do prisma triângular        ||||')
    print('||||      3 - Total das áreas do prisma triângular     ||||')
    print('||||      4 - Volume do prisma triângular              ||||')
    print('||||      5 - Área da base do prisma hexagonal         ||||')
    print('||||      6 - Área lateral do prisma hexagonal         ||||')
    print('||||      7 - Total das áreas do prisma hexagonal      ||||')
    print('||||      8 - Volume do prisma hexagonal               ||||')
    print('||||      9 - Encerrar programa                        ||||')

    opcao = int(input())

    if opcao == 1:
        print('Opções:\n')
        print('1 - Calcular a área somente com lados')
        print('2 - Calcular com base e altura\n')
        calculo = int(input())
        if calculo == 1:
            lado = float(input('Informe o valor do lado: '))
            areaBaseSemAltura(lado)
        elif calculo == 2:
            lado = float(input('Informe o valor do lado: '))
            altura = float(input('Informe o valor da altura: '))
            areaBaseComAltura(lado, altura)
        else:
            print('Opção inválida\n')

    elif opcao == 2:
        aresta = float(input('Informe o valor da aresta da base: '))
        altura = float(input('Informe o valor da altura: '))
        areaLateral(aresta, altura)
        print('Opções:\n')
        print('1 - Calcular área total das laterais')
        print('2 - Sair')
        calculo = int(input())
        if calculo == 1:
            areaTotalLateral(aresta, altura)
        elif calculo == 2:
            print('Encerrada\n')
            laco = False
        else:
            print('Opção inválida\n')

    elif opcao == 3:
        print('Opções:\n')
        print('1 - Área total usando valores de áreas')
        print(
            '2 - Área total usando aresta da base, altura do triângulo e altura do prisma')
        print('3 - Área total usando aresta da base e altura')
        calculo = int(input())
        if calculo == 1:
            areaBase = float(input('Informe a área da base: '))
            arealateral = float(input('Informe a área da lateral: '))
            areaTotalComBases(areaBase, arealateral)
        elif calculo == 2:
            aresta = float(input('Informe o valor da aresta da base: '))
            alturatriangulo = float(input('Informe a altura do triângulo: '))
            altura = float(input('Informe a altura do prisma: '))
            areaTotalPrisma2(aresta, alturatriangulo, altura)
        elif calculo == 3:
            aresta = float(input('Informe o valor da aresta da base: '))
            altura = float(input('Informe o valor da altura do prisma: '))
            areaTotalPrisma1(aresta, altura)
        else:
            print('Opção inválida\n')

    elif opcao == 4:
        print('Opções:\n')
        print('1 - Calcular volume usando área')
        print('2 - Calcular volume usando somente medidas')
        calculo = int(input())
        if calculo == 1:
            areaBase = float(input('Informe a área da base: '))
            altura = float(input('Informe o valor da altura: '))
            volumeComArea(areaBase, altura)
        elif calculo == 2:
            aresta = float(input('Informe o valor da aresta da base: '))
            altura = float(input('Informe o valor da altura: '))
            volumeSemArea(aresta, altura)
        else:
            print('Opção inválida\n')

    elif opcao == 5:
        lado = float(input('Informe o valor da aresta da base: '))
        areaBaseHex(lado)

    elif opcao == 6:
        lado = float(input('Informe o valor da aresta da base: '))
        altura = float(input('Informe o valor da altura do prisma: '))
        areaLateralHex(lado, altura)
        print('Opções:\n')
        print('1 - Calcular total das áreas laterais')
        print('2 - Sair')
        calculo = int(input())
        if calculo == 1:
            areaTotalLateralex(lado, altura)
        elif calculo == 2:
            print('Encerrado\n')
            laco = False
        else:
            print('Opção inválida\n')

    elif opcao == 7:
        print('Opções:\n')
        print('1 - Calcular área total com medidas')
        print('2 - Calcular área total com valores das áreas')
        calculo = int(input())
        if calculo == 1:
            aresta = float(input('Informe o valor da aresta da base: '))
            altura = float(input('Informe o valor da altura do prisma: '))
            areaTotalComMedidasHex(aresta, altura)
        elif calculo == 2:
            areaBase = float(input('Informe o valor da área da base: '))
            arealateral = float(input('Informe o valor da área lateral: '))
            areaTotalComAreasHex(areaBase, arealateral)
        else:
            print('Opção inválida\n')

    elif opcao == 8:
        print('Opções:\n')
        print('1 - Calcular volume com área e altura')
        print('2 - Calcular volume somente com medidas')
        calculo = int(input())
        if calculo == 1:
            areaBase = float(input('Informe o valor da área da base: '))
            altura = float(input('Informe o valor da altura do prisma: '))
            volumePrismaHex(areaBase, altura)
        elif calculo == 2:
            lado = float(input('Informe o valor da aresta da base: '))
            altura = float(input('Informe o valor da altura do prisma: '))
            volumePrismaComMedidas(lado, altura)

    elif opcao == 9:
        laco = False

    else:
        print('Opção inválida\n')
