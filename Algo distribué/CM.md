# Algorithme distribué

- contact : flavien.vernier@univ-smb.fr
- clé moodle :

## 1. Introduction

def : un algorithme distribué est un algorithme qui s'exécute sur un ensemble de machines connectées par un réseau.

def de Lamport : cf cours

## 2. Diffusion

### 2.1. Diffusion centralisée

```python
def BrodcastCentral(myId):
    if myId == 0:
        for i in range(1, nbProc-1):
            send(i, "Hello")
    else:
        msg = receive(0)
        print(msg)
```

### 2.2. Diffusion en anneau

```python
def BrodacastRingOneSide(myId):
    if myId == 0:
        send(1, "Hello")
    elif myId == nbProc-1:
        msg = receive(myId-1)
    else:
        msg = receive(myId-1)
        send((myId+1), msg)
```

**/!\\** Formule avec modulo pour ce deplacer dans l'anneau

```python
prev = (myId - 1 + nbProc) % nbProc
next = (myId + 1) % nbProc
```

## 3. Scatter

### 3.1. Scatter centralisé

```python
def ScatterCentral(myId, data):
    sizePart = len(data)//nbProc

    if myId == 0:
        # On commence a sizePart car le noeud 0 garde la premiere partie
        for i in range(sizePart, len(data)-1, sizePart):
            # Si on est pas a la derniere partie
            if i+sizePart < len(data):
                send(i, data[i:i+sizePart])
            # Si on est a la derniere partie
            else:
                send(i, data[i:])
    else:
        msg = receive(0)
        print(msg)
```
