var Storage = {
    add : function (key,value){
      localStorage.setItem(key, value);
    },
    load: function (key){
      return localStorage.getItem(key);
    }
}

var Server_settings = {
  url : 'http://localhost:10000/',
}
