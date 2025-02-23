from django.shortcuts import render
from gameshop.models import Game
from gameshop.forms import GameModelForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  # Import necessário para bloquear telas para os usuários não logados
from django.utils.decorators import method_decorator
from gemini_api.client import game_bio_generator


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'
    context_object_name = 'games'

    def get_queryset(self):
        games = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            games = games.filter(
                Q(name__icontains=search) | Q(producer__name__icontains=search)
            )
        return games


@method_decorator(login_required(login_url='login'), name='dispatch')
class GamesCreateView(CreateView):
    model = Game
    form_class = GameModelForm
    template_name = 'new_game.html'
    success_url = '/games/'

    def form_valid(self, form):
        # Gere a bio para o jogo antes de salvar
        game = form.save(commit=False)
        game_bio = game_bio_generator(game.name)  # Gere a bio
        print(game_bio)
        if game_bio:
            game.bio = game_bio  # Armazena a bio no campo correto
            game.save()
        game.description = game_bio  # Assuma que você tem um campo 'description' para armazenar a bio
        game.save()
        return super().form_valid(form)


class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class GameUpdateView(UpdateView):
    model = Game
    template_name = 'game_update.html'
    form_class = GameModelForm

    def get_success_url(self):
        return reverse_lazy('game_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        # Gere a bio para o jogo antes de salvar
        game = form.save(commit=False)
        game_bio = game_bio_generator(game.name)  # Gere a bio
        if game_bio:
            game.bio = game_bio  # Armazena a bio no campo correto
            game.save()
        game.description = game_bio  # Assuma que você tem um campo 'description' para armazenar a bio
        game.save()
        return super().form_valid(form)
    


@method_decorator(login_required(login_url='login'), name='dispatch')
class GameDeleteView(DeleteView):
    model = Game
    template_name = 'game_delete.html'
    success_url = '/games/'
