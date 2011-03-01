Ext.ns("Phi.model");
/**
 * @class Phi.model.Entity 
 * @extends Ext.util.Observable
 * 
 * Philosophy abstract generic CRUD Entity 
 * 
 * @author rbarriga
 * @version 1.0
 * @copyright (c) 2011, by rbarriga
 * @date      15. February 2011
 *
 */
Phi.model.Entity = Ext.extend(Ext.util.Observable, {
	constructor: function (config) {
		this.addEvents(
			/**
			* @event create Event declaration
			*/
			'create',
			/**
			* @event read Event declaration
			*/
			'read',
			/**
			* @event update Event declaration
			*/
			'update',
			/**
			* @event remove Event declaration
			*/
			'remove'
		);
		Phi.model.Entity.superclass.constructor.call(config);
	}
	,
	/**
	* Create entity
	* @param {Object} object entity definition
	*/
	create: function (o) {
		Ext.Ajax.request({
			url: this.entityURL,
			method: 'POST',
			headers: { 'Content-Type': 'text/json' },
			jsonData: o,
			scope:this,
			success: function (r, opt) {
				this.fireEvent('create', o);
			}
		})
	}
	,
	/**
	* Read entity
	* @param {String} entity identification (key)
	*/
	read: function (id) {
		Ext.Ajax.request({
			url: this.entityURL + '/' + id,
			scope:this,
			success: function (r, opt) {
				var o = Ext.util.JSON.decode(r.responseText);
				this.fireEvent('read', o);
			}
		});
	}
	,
	/**
	* Update entity
	* @param {Object} object entity definition
	*/
	update: function (o) {
		Ext.Ajax.request({
			url: this.entityURL,
			method: 'PUT',
			headers: { 'Content-Type': 'text/json' },
			jsonData: o,
			scope:this,
			success: function (r, opt) {
				this.fireEvent('update', o);
			}
		});
	}
	,
	/**
	* Remove (delete)entity
	* @param {String} entity identification (key)
	*/
	remove: function (id) {
		Ext.Ajax.request({
			url: this.entityURL + '/' + id,
			method: 'DELETE',
			scope:this,
			success: function (r, opt) {
				this.fireEvent('remove', r);
			}
		});
	}
});