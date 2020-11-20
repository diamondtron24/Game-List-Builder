let app = new Vue({
    el: "#app",
    delimiters: ['xxx','xxx'],
    data: {
        message: 'hello',
        // [] = lists, {} = dictionaries
        // base variables are lists of all available. 
        // specific ships/squads/objects are dictonaries
        baseShips : [],
        ship : {},
        baseSquadrons : [],
        squadrons : {},
        baseObjectives : [],
        objectives : {},
    },

    methods: {
        getBaseShips: async function(){
            data = await axios.get('getBaseShips/')
            console.log(data)
            app.baseShips = data.data.base_ships
        }

    },
    
    created: function(){

    }
})