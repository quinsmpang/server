
�
	Msg.proto"4
Package
name (	
rpcId (
data ("
S2C_Ping
time ("
C2S_Ping
time (">
C2S_RegisterAccount
accountName (	

accountPwd (	"%
S2C_RegisterAccount
result ("4
	C2S_Login
accountName (	

accountPwd (	"L
	S2C_Login
result (
address (	
port (
playerId ("

C2S_Online
playerId ("B

S2C_Online
result (
playerId (

playerName (	"

name (	"�
S2C_RoomData
roomId (
roomName (	
	captianId ((

playerList (2.S2C_RoomData.Player=
Player
playerId (

playerName (	
ready ("
C2S_BroadcastRoomData"?
S2C_LoadBattle
battle (
address (	
port ("2
C2S_JoinBattle
playerId (
battle ("
S2C_StartBattle"�
S2C_CreateUnit*
unitList (2.S2C_CreateUnit.UnitInfoL
UnitInfo
guid (
unitId (	
x (	
y (
data (	".
Player
playerId (

playerName (	"4
Request_RoomList
startIdx (
endIdx ("�
Response_RoomList-
roomList (2.Response_RoomList.RoomInfoV
RoomInfo
roomId (
roomName (	

totalCount (
currentCount ("
Request_CreateRoom"5
Response_CreateRoom
result (
roomId (""
Request_JoinRoom
roomId ("#
Response_JoinRoom
result ("
Request_StartGame"$
Response_StartGame
result ("#
Request_PrepareGame
flag (