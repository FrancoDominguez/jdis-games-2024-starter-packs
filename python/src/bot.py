from typing import List, Union

from core.action import MoveAction, ShootAction, RotateBladeAction, SwitchWeaponAction, SaveAction
from core.consts import Consts
from core.game_state import GameState, PlayerWeapon, Point, PlayerInfo
from core.map_state import MapState
import math as math


class MyBot:
     __map_state: MapState
     name : str
     
     game_date = {
          "explored":[]
     }


     def __init__(self):
          self.name = "Magellan"


     def on_tick(self, game_state: GameState) -> List[Union[MoveAction, SwitchWeaponAction, RotateBladeAction, ShootAction, SaveAction]]:
          players = game_state.players
          my_name = "Boule de Sac"


          me = -1
          for index, player in enumerate(players):
               if player.name == my_name:
                    me = players[index]
          

          nearestPos = self.getNearestPos(me , game_state)

          print(me.playerWeapon)


          actions = [
               MoveAction((nearestPos[2] , nearestPos[3])),
               ShootAction((nearestPos[0].x , nearestPos[0].y)),
          ]
          if me.playerWeapon != 1:
               actions.append(SwitchWeaponAction(PlayerWeapon.PlayerWeaponCanon))
                    
          return actions
    
    
     def on_start(self, map_state: MapState):
          self.__map_state = map_state

          actions = [
               SwitchWeaponAction(PlayerWeapon.PlayerWeaponCanon)
          ]

          return actions


     def on_end(self):
          pass

     def getNearestPos(self, me: PlayerInfo, game_state: GameState):
          minDistance = float('inf')
          closestPlayer = None



          for player in game_state.players:
               if player == me:
                    continue  

               playerDistance = math.sqrt((player.pos.x - me.pos.x)**2 + (player.pos.y - me.pos.y)**2)
               if playerDistance < minDistance:
                    minDistance = playerDistance
                    closestPlayer = player
          print("enemy: ", closestPlayer.name)
          stratX, stratY = self.getStrategicPosition(me.pos.x, me.pos.y, closestPlayer.pos.x, closestPlayer.pos.y)
          

          if closestPlayer is not None:
               return [closestPlayer.pos , minDistance , stratX , stratY]
          return None




     def getStrategicPosition(self, X1, Y1, X2, Y2):
          d = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
    
          dx_perp = -(Y2 - Y1)
          dy_perp = X2 - X1
          
          # Normalize the perpendicular vector
          length = math.sqrt(dx_perp ** 2 + dy_perp ** 2)
          dx_perp /= length
          dy_perp /= length
          
          # Scale by distance d
          dx_perp *= d
          dy_perp *= d
          
          # Calculate point C
          Xc = X2 + dx_perp
          Yc = Y2 + dy_perp
          
          return Xc, Yc

          return