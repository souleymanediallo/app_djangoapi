import graphene
from graphene_django import DjangoObjectType
from .models import Movie, Director


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        description = graphene.String()

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, title, description):
        movie = Movie.objects.get(pk=id)
        movie.title = title
        movie.description = description
        movie.save()

        return MovieUpdateMutation(movie=movie)


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        director_id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, description, director_id):
        movie = Movie(title=title, description=description, director_id=director_id)
        movie.save()

        return MovieCreateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id):
        movie = Movie.objects.get(pk=id)
        movie.delete()

        return MovieDeleteMutation(movie=None)


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    all_directors = graphene.List(DirectorType)
    movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_all_directors(self, info, **kwargs):
        return Director.objects.all()

    def resolve_move(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Movie.objects.get(pk=id)

        if title is not None:
            return Movie.objects.get(title=title)

        return None


schema = graphene.Schema(query=Query)