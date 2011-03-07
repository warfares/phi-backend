/*
  phi-model.js 
  Copyright 2005-2011 :-), Inc., released under the Clear BSD  license.

  Includes compressed code under the following licenses:

  (For uncompressed versions of the code used please see the
  phi-model GIT repository: ...)
*/
Ext.ns("Phi");Ext.ns("Philosophy");Philosophy=Phi;Phi.WSGIScriptAlias='phi-rest';Phi.UriTemplate={users:'/user/all',user:'/user',userLogin:'/user/login',userSetPassword:'/user/setpassword',userGetLocations:'/user/getlocations',userGetFavLocations:'/user/getfavlocations',userGetLayers:'/user/getlayers',userSearchLayer:'/user/searchlayers',userGetNodes:'/user/getnodes',userGetRasters:'/user/getrasters',layer:'/layer',location:'/location',locationFavorite:'/location/favorite',workspace:'/workspace',workspaceGetByOwner:'/workspace/get_by_owner',getUri:function(action,option){var hostname='http://'+window.location.hostname+'/';return hostname+Phi.WSGIScriptAlias+Phi.UriTemplate[action]+(option||'');}};Ext.ns("Phi.model");Phi.model.Entity=Ext.extend(Ext.util.Observable,{constructor:function(config){this.addEvents('create','read','update','remove');Phi.model.Entity.superclass.constructor.call(config);},create:function(o){Ext.Ajax.request({url:this.entityURL,method:'POST',headers:{'Content-Type':'text/json'},jsonData:o,scope:this,success:function(r,opt){this.fireEvent('create',o);}})},read:function(id){Ext.Ajax.request({url:this.entityURL+'/'+id,scope:this,success:function(r,opt){var o=Ext.util.JSON.decode(r.responseText);this.fireEvent('read',o);}});},update:function(o){Ext.Ajax.request({url:this.entityURL,method:'PUT',headers:{'Content-Type':'text/json'},jsonData:o,scope:this,success:function(r,opt){this.fireEvent('update',o);}});},remove:function(id){Ext.Ajax.request({url:this.entityURL+'/'+id,method:'DELETE',scope:this,success:function(r,opt){this.fireEvent('remove',r);}});}});Ext.ns("Phi.model");Phi.model.User=Ext.extend(Phi.model.Entity,{entityURL:Phi.UriTemplate.getUri('user'),initComponent:function(config){this.addEvents('login','setpassword','getfavoriteslocations','getnodes','getrasters','getlayers');Phi.model.User.superclass.initComponent.call(config);},login:function(userName,password){var credentials={userName:userName,password:password}
var valid=false;Ext.Ajax.request({url:Phi.UriTemplate.getUri('userLogin'),method:'POST',headers:{'Content-Type':'text/json'},jsonData:credentials,scope:this,success:function(response,options){var o=Ext.util.JSON.decode(response.responseText);var status=o.success;var user=o.user;this.fireEvent('login',status,credentials,user);}});},setPassword:function(userName,password){var o={userName:userName,password:password}
Ext.Ajax.request({url:Phi.UriTemplate.getUri('userSetPassword'),method:'POST',headers:{'Content-Type':'text/json'},jsonData:o,scope:this,success:function(response,options){var response=Ext.util.JSON.decode(response.responseText);this.fireEvent('setpassword',response);}});},getFavoritesLocations:function(userName){var p={userName:userName};Ext.Ajax.request({url:Phi.UriTemplate.getUri('userGetFavLocations','?'+Ext.urlEncode(p)),method:'GET',headers:{'Content-Type':'text/json'},scope:this,success:function(response,options){var collection=Ext.util.JSON.decode(response.responseText);locations=collection.entities
this.fireEvent('getfavoriteslocations',locations);}});},getRasters:function(userName){var p={userName:userName};Ext.Ajax.request({url:Phi.UriTemplate.getUri('userGetRasters','?'+Ext.urlEncode(p)),method:'GET',headers:{'Content-Type':'text/json'},scope:this,success:function(response,options){var collection=Ext.util.JSON.decode(response.responseText);rasters=collection.entities
this.fireEvent('getrasters',rasters);}});},getNodes:function(userName){var p={userName:userName};Ext.Ajax.request({url:Phi.UriTemplate.getUri('userGetNodes','?'+Ext.urlEncode(p)),method:'GET',headers:{'Content-Type':'text/json'},scope:this,success:function(response,options){var n=Ext.util.JSON.decode(response.responseText);var nodes=[];nodes.push(n);this.fireEvent('getnodes',nodes);}});},getLayers:function(userName){var p={userName:userName};Ext.Ajax.request({url:Phi.UriTemplate.getUri('userGetLayers','?'+Ext.urlEncode(p)),method:'GET',headers:{'Content-Type':'text/json'},scope:this,success:function(response,options){var o=Ext.util.JSON.decode(response.responseText);this.fireEvent('getlayers',o.entities);}});}});Ext.ns("Phi.model");Phi.model.Layer=Ext.extend(Phi.model.Entity,{entityURL:Phi.UriTemplate.getUri('layer'),initComponent:function(config){Phi.model.Layer.superclass.initComponent.call(config);}});Ext.ns("Phi.model");Phi.model.Location=Ext.extend(Phi.model.Entity,{entityURL:Phi.UriTemplate.getUri('location'),initComponent:function(config){this.addEvents('favorite');Phi.model.Location.superclass.initComponent.call(config);},favorite:function(id,favorite){var o={id:id,favorite:favorite}
Ext.Ajax.request({url:Phi.UriTemplate.getUri('locationFavorite'),method:'POST',headers:{'Content-Type':'text/json'},jsonData:o,scope:this,success:function(response,options){var response=Ext.util.JSON.decode(response.responseText);this.fireEvent('favorite',response);}});}});Ext.ns("Phi.model");Phi.model.Workspace=Ext.extend(Phi.model.Entity,{entityURL:Phi.UriTemplate.getUri('workspace'),initComponent:function(config){Phi.model.Workspace.superclass.initComponent.call(config);}});