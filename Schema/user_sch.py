from typing import List
def Schema_user(usuarios) -> dict:
    return  {"user_id" : usuarios[0],
                "nombre" : usuarios[1],
                "cogno" : usuarios[2],
                "correo" : usuarios[3],
                "descripcion" : usuarios[4],
                "curso" : usuarios[5],
                "any" : usuarios[6],
                "direccio" : usuarios[7],
                "codgiP" : usuarios[8],
                "password" : usuarios[9]
                
    }
  
def users_schema(users) -> List[dict]:
    return  [Schema_user(usuarios) for usuarios in users] 