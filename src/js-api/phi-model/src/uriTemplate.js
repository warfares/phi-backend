Ext.ns("Phi");
Ext.ns("Philosophy");
Philosophy = Phi;

//TODO fix this staic value.. !! 
Phi.WSGIScriptAlias = 'phi-rest';

/**
* @class Phi.UriTemplate
* @singleton
*
* Philosophy Simple hash table with python mod_wsgi rest services uri templates
* 
* @author rbarriga
* @version 1.0
* @copyright (c) 2011, by rbarriga
* @date     15. February 2011
*
*/
Phi.UriTemplate = {
	users: '/user/all',
	user: '/user',
	userLogin: '/user/login',
	userSetPassword: '/user/setpassword',
	userSearch: '/user/search',
	
	//user locations
	userGetLocations: '/user/getlocations',
	userGetFavLocations: '/user/getfavlocations',

	//user workspace
	userSearchWorkspace: '/user/searchworkspace',
	
	//user layers
	userGetLayers: '/user/getlayers',
	userSearchLayer : '/user/searchlayers',

	//user nodes
	userGetNodes: '/user/getnodes',

	//user rasters
	userGetRasters: '/user/getrasters',  

	//layer service
	layer: '/layer',
	
	//location 
	location: '/location',
	locationFavorite: '/location/favorite',
	
	//workspace service
	workspace: '/workspace',
	workspaceGetByOwner: '/workspace/getbyowner',  
	workspaceGetUsers: '/workspace/getusers', 
	
	workspaceAddUsers: '/workspace/addusers',  
	workspaceRemoveUsers: '/workspace/removeusers',

	getUri: function(action, option) {
		var hostname = 'http://' + window.location.hostname + '/';
		return hostname + Phi.WSGIScriptAlias + Phi.UriTemplate[action] + (option || '');
	}
};// eo Phi.Uritemplate
// eof