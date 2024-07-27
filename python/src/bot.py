from typing import List, Union

from core.action import MoveAction, ShootAction, RotateBladeAction, SwitchWeaponAction, SaveAction
from core.consts import Consts
from core.game_state import GameState, PlayerWeapon, Point, PlayerInfo
from core.map_state import MapState
import math as math


class MyBot:
     """
     (fr) Cette classe représente votre bot. Vous pouvez y définir des attributs et des méthodes qui 
          seront conservées entre chaque appel de la méthode `on_tick`.

     (en) This class represents your bot. You can define attributes and methods in it that will be kept 
          between each call of the `on_tick` method.
     """
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
          
          """

                    - MoveAction((x, y))        Directs your bot to move to the specified point at a constant speed.
                    - ShootAction((x, y))       If you have the gun equipped, it will shoot at the given coordinates.
                    - SaveAction([...])         Allows you to store 100 bytes on the server. When you reconnect, these 
                                                data will be provided to you by the server.
                    - SwitchWeaponAction(id)    Allows you to change your weapon. By default, your bot is unarmed. Here 
                                                are your choices:
                                                  PlayerWeapon.PlayerWeaponNone
                                                  PlayerWeapon.PlayerWeaponCanon
                                                  PlayerWeapon.PlayerWeaponBlade
                    - BladeRotateAction(rad)    if you have the blade as a weapon, you can set your
                                                weapon to the given rotation in radians.

          Arguments:
               game_state (GameState): The state of the game.   
          """
          # print(f"Current tick: {game_state.current_tick}")

          nearestPos = self.getNearestPos(me , game_state)

          print(me.playerWeapon)


          actions = [
               MoveAction((nearestPos[0].x , nearestPos[0].y)),
               ShootAction((nearestPos[0].x , nearestPos[0].y)),
          ]
                    
          return actions
    
    
     def on_start(self, map_state: MapState):
          """

               This method is called once at the beginning of the game. You can define actions to be 
               performed at the beginning of the game.

          Arguments:
               map_state (MapState): (fr) L'état de la carte.
                                   (en) The state of the map.
          """
          self.__map_state = map_state

          actions = [
               SwitchWeaponAction(PlayerWeapon.PlayerWeaponCanon)
          ]

          return actions


     def on_end(self):
          """
               This method is called once at the end of the game. You can define actions to be performed 
               at the end of the game.
          """
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

          if closestPlayer is not None:
               return [closestPlayer.pos , minDistance]
          return None  # In case no closest player was found
