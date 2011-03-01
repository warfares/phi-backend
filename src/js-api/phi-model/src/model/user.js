Ext.ns("Phi.model");
/**
 * @class Phi.model.User
 * @extends Phi.model.Entity
 * 
 * Philosophy User Proxy
 * <br/>
 * Example:
<pre><code>
var user = new Phi.model.User()

user.on('read', somefunction, this) // somefunction  on the XHR async success 
user.Read('someUser'); //  The async call 
</code></pre>
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 * @date      15. February 2011
 */
Phi.model.User = Ext.extend(Phi.model.Entity, {
	entityURL: Phi.UriTemplate.getUri('user'),

	initComponent: function (config) {
		this.addEvents(
			/**
			* @event login Event declaration
			*/
			'login',
			'getfavoriteslocations',
			'getnodes',
			'getrasters',
			'getlayers'
		);
		Phi.model.User.superclass.initComponent.call(config);
	}
	,
	/**
	* User login access
	* @param {String} userName user name (key)
	* @param {String} password user password
	* */
	login: function (userName, password) {

		var credentials = {
			user_name: userName,
			password: password
		}

		var valid = false;

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('userLogin'),
			method: 'POST',
			headers: { 'Content-Type': 'text/json' },
			jsonData: credentials,
			scope: this,
			success: function (response, options) {

				var o = Ext.util.JSON.decode(response.responseText);
				var status = o.status;
				var user = o.user;

				this.fireEvent('login', status, credentials, user);
			}
		});
	}
	,
	/**
	* User favorite Locations
	* @param {String} userName user name (key)
	* */
	getFavoritesLocations: function(userName){
		var p = { userName: userName };

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('userGetFavLocations', '?' + Ext.urlEncode(p)),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var collection = Ext.util.JSON.decode(response.responseText);
				locations = collection.entities
				this.fireEvent('getfavoriteslocations', locations);
			}
		});
	}
	,
	/**
	* User rasters
	* @param {String} userName user name (key)
	* */
	getRasters: function (userName) {
		var p = { userName: userName };

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('userGetRasters', '?' + Ext.urlEncode(p)),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var collection  = Ext.util.JSON.decode(response.responseText);
				rasters = collection.entities
				this.fireEvent('getrasters', rasters);
			}
		});

	}
	,
	/**
	* User layer nodes (tree structure)
	* @param {String} userName user name (key)
	* */
	getNodes: function (userName) {
		var p = { userName: userName };

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('userGetNodes', '?' + Ext.urlEncode(p)),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var n = Ext.util.JSON.decode(response.responseText);
				var nodes = [];
				nodes.push(n);
				this.fireEvent('getnodes', nodes);
			}
		});
	}
	,
	/**
	* User Layers
	* @param {String} userName user name (key)
	* */
	getLayers: function (userName) {
		var p = { userName: userName };

		Ext.Ajax.request({
			url: Phi.UriTemplate.getUri('userGetLayers', '?' + Ext.urlEncode(p)),
			method: 'GET',
			headers: { 'Content-Type': 'text/json' },
			scope: this,
			success: function (response, options) {
				var o = Ext.util.JSON.decode(response.responseText);
				this.fireEvent('getlayers', o.entities);
			}
		});
	}
});