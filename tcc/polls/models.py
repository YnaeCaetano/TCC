from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique= True)
    senha = models.CharField(max_length=100)
    foto_perfi = models.ImageField(upload_to= 'imagens')

    def __str__(self):
        return self.nome
    

class Endereço(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    CEP = models.CharField(max_length=9)
    id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self
    
class Categoria(models.Model):
     nome = models.CharField(max_length=100)
     descricao = models.CharField(max_length=100)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=6, verbose_name= "preço")
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to= 'imagens')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

def __str__(self):
        return self.nome 

class Carrinho(models.Model):
     id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     id_Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Item_Carrinho(models.Model):
     id_Carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)     
     id_Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
     quantidade = models.IntegerField()

class Pedido(models.Model):
     id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     data_pedido = models.DateField(max_length=100)
     status = models.CharField(max_length= 100)
     total = models.DecimalField(decimal_places=2, max_digits= 100, verbose_name= "total")

class Item_Pedido(models.Model):
     id_Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
     id_Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     preco_unitario = models.DecimalField(decimal_places=2, max_digits= 100, verbose_name= "preço unitario")

class Pagamento(models.Model):
     id_Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
     metodo_pagamento = models.CharField(max_length= 100)
     status = models.CharField(max_length= 100)

class Comentario(models.Model):
     id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     descricao = models.CharField(max_length=400)

class Evento(models.Model):
     nome = models.CharField(max_length= 100)
     data = models.DateField(max_length=100)