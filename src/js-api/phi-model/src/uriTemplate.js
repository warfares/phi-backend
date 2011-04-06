Ext.ns("Phi");
Ext.ns("Philosophy");
Philosophy = Phi;

/**
* @class Phi.UriTemplate
* @singleton
*
* Philosophy Simple hash table with python mod_wsgi rest services 
* or .Net WCF Services uri templates
* 
* @author rbarriga
* @version 1.0
* @copyright (c) 2011, by rbarriga
* @date     15. February 2011
*
*/

Phi.Net = false;

var userService = Phi.Net ? 'svc/UserService.svc/rest' : 'phi-rest';
var layerService = Phi.Net ? 'svc/LayerService.svc/rest' : 'phi-rest';
var locationService = Phi.Net ? 'svc/LocationService.svc/rest' : 'phi-rest';
var workspaceService = Phi.Net ? 'svc/WorkSpaceService.svc/rest' : 'phi-rest';
var groupService = Phi.Net ? 'svc/GroupService.svc/rest' : 'phi-rest';
var utilService = Phi.Net ? 'svc/UtilService.svc/rest' : 'phi-rest';


Phi.UriTemplate = {
	users: userService + '/user/all',
	user: userService + '/user',
	userLogin: userService + '/user/login',
	userLogout : userService + '/user/logout',
	userIsauth : userService + '/user/isauth',
	userSetPassword: userService + '/user/setpassword',
	userSearch: userService + '/user/search',
	
	//user locations
	userGetLocations: userService + '/user/getlocations',
	userGetFavLocations: userService + '/user/getfavlocations',

	//user workspace
	userSearchWorkspace: workspaceService + '/user/searchworkspace',
	
	//user layers
	userGetLayers: userService + '/user/getlayers',
	userSearchLayer : userService + '/user/searchlayers',

	//user nodes
	userGetNodes: userService + '/user/getnodes',

	//user rasters
	userGetRasters: userService + '/user/getrasters',

	//eof user

	//layer service
	layer: layerService +'/layer',
	layerGetFiles : layerService + '/layer/getfiles',

	//location 
	location: locationService + '/location',
	locationFavorite: locationService +'/location/favorite',
	
	//workspace service
	workspace: workspaceService + '/workspace',
	workspaceGetByOwner: workspaceService + '/workspace/getbyowner',  
	workspaceGetUsers: workspaceService + '/workspace/getusers', 
	
	workspaceAddUsers: workspaceService + '/workspace/addusers',  
	workspaceRemoveUsers: workspaceService + '/workspace/removeusers',
	
	//group 
	group: groupService + '/group',
	groups: groupService + '/group/all',
	
	//role
	role: utilService + '/role',
	roles: utilService + '/role/all',
	
	getUri: function(action, option) {
		var hostname = 'http://' + window.location.hostname + ':' + window.location.port +  '/';
		return hostname + Phi.UriTemplate[action] + (option || '');
	}
};// eo Phi.Uritemplate
// eof
