from django.db import models
#Para importar imagens: python -m pip install Pillow


class Autor(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    data_nascimento = models.DateField("Data nascimento", blank=True, null=True)
    pais = models.CharField("Pais", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    categoria = models.CharField("Categoria", max_length=200)
    descricao = models.TextField("Descrição")

    def __str__(self):
        return self.categoria


class Valor(models.Model):
    valor = models.DecimalField("Valor", max_digits=7, decimal_places=2, default=99.99)

    def __str__(self):
        return self.valor


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=200)
    autor = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria", blank=True, null=True)
    data_publicacao = models.DateField("Data publicação", blank=True, null=True)
    edicao = models.CharField("Edição", max_length=200, blank=True, null=True)
    genero = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    editora = models.CharField("Editora", max_length=200, blank=True, null=True)
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, verbose_name="Valor", blank=True, null=True)
    #imagem = models.ImageField(upload_to='livraria/media', blank=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a "
                                                                          "href='https://www.isbn-international.org/content/what-isbn""'>ISBN number</a>")

    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo


class Endereco(models.Model):
    rua = models.CharField("Rua", max_length=200, null=True)
    numero = models.IntegerField("Número", null=True)
    bairro = models.CharField("Bairro", max_length=100, null=True)
    cidade = models.CharField("Cidade", max_length=50, null=True)
    estado = models.CharField("Estado", max_length=100, null=True)
    cep = models.IntegerField("CEP", null=True)
    pais = models.CharField("Cidade", max_length=50, null=True)


class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
        ('I', u'Intersexo'),
        ('N', u'Não declarar'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )

    nome = models.CharField("Nome Completo", max_length=200)
    data_nascimento = models.DateField("Data nascimento", blank=True, null=True)
    cpf = models.CharField("CPF", max_length=120, null=True)
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField("Estado civil", max_length=1, choices=ESTADO_CIVIL_CHOICES)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name="Endereco", blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    telefone = models.CharField("Nº telefone celular", max_length=11, blank=True, null=True)

    def __str__(self):
        return self.nome


class Shop(models.Model):
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Nome do Cliente", blank=True, null=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "compra"
        verbose_name_plural = "compras"

    def __str__(self):
        return self.nome_cliente


class Carrinho(models.Model):
    shop = models.ForeignKey(Shop, related_name="Compras", on_delete=models.CASCADE)
    produto = models.ForeignKey(Livro, related_name="Produto", on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.PositiveIntegerField("Quantidade")
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE, verbose_name="Valor", blank=True, null=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "carrinho"
        verbose_name_plural = "carrinhos"

    def __str__(self):
        if self.shop:
            return f'{self.shop.pk}-{self.pk}-{self.produto}'
        return str(self.pk)

    def get_subtotal(self):
        return self.preco * (self.quantidade or 0)