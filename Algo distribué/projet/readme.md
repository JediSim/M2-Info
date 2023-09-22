# API Communication

## Mise en place

- Créer un communicateur

```python
com = Com()
```

- Connecter les communicateurs

```python
# Pour chaques processus
com.connect()
```

- Pour la gestion de la section critique le dernier processus créé doit appeler la fonction suivante pour lancer le token dans le systeme

```python
self.com.releaseSC()
```

## Features

### Communication

- Envoyer un message à un autre processus

`com.sendTo(message, sender)`

```python
self.com.sendTo("Hello World", "P1")
```

- Envoyer un message à un autre processus de manière synchrone

`com.sendToSync(message, sender)`

```python
self.com.sendToSync("OK", "P0")
```

le processus courant attendra la reception du processus P0
`com.recevFromSync(sender)`

```python
msg = self.com.recevFromSync("P2")
```

Le processus P0 attendra la reception du message du processus qui envoie le message (ici P2)

- Envoyer un message à tous les autres processus

`com.broadcast(message, sender)`

```python
self.com.broadcast("coucou tout le monde", self.getName())
```

- Envoyer un message à tous les autres processus de manière synchrone

`com.broadcastSync(message, sender)`

```python
self.com.broadcastSync(self.getName(), "P0 est synchro")
```

Les autres processus attendront la reception du message du processus qui envoie le message (ici P0)
`com.broadcastSync(sender)`

```python
self.com.broadcastSync("P0")
```

### Section Critique

- Entrer en section critique

```python
self.com.requestSC()
```

- Sortir de section critique

```python
self.com.releaseSC()
```

### Syncronisation

- Attendre que tous les processus soient prêts

```python
self.com.synchronize()
```

Tous les processus devoient appeler cette fonction pour qu'ils puissent continuer
