let app = new Vue({
    el: "#app",
    delimiters: ['xxx','xxx'],
    data: {
        message: 'hello',
        // [] = lists, {} = dictionaries
        // base variables are lists of all available. 
        // specific ships/squads/objects are dictonaries
        baseShips : [],
        SelectedShip : {},
        baseSquadrons : [],
        squadrons : {},
        baseObjectives : [],
        objectives : {},
        shipUpgrades : [],
    },

    methods: {
        getBaseShips: async function(faction){
            data = await axios.get(`getBaseShips/${faction}/`)
            console.log(data)
            app.baseShips = data.data.base_ships
            
        },

        selectShip: async function(ship_id){
            console.log(ship_id)
            data = await axios.get(`getSingleShip/${ship_id}/`)
            app.SelectedShip = data.data.ship
            app.baseShips = []
            app.shipUpgrades = data.data.upgrades
        }

        
            
    },
    
    created: function(){

    }
})