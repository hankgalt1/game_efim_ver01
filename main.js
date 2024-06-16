// @ts-ignore
import phaser from './phaser.js';
import { SCENE_KEYS } from './scene-keys.js';
import {PreloadScene} from './scene/preload-scene.js'
import {GameScen} from './scene/game_scene.js'
import { GameOver } from './scene/game_over.js';
const width = window.innerWidth;
const height = window.innerHeight;


const game = new Phaser.Game({
    type:Phaser.CANVAS,
    physics:{
        default:'arcade',
        arcade:{
            gravity:{
                y: 300,
                x: 0
            },
            debug:false
        }
    },
    pixelArt:false,
    dom: {
		createContainer: true
	},
    scale:{
        parent: 'game-container',
        width:width,
        height:height,
        
        mode:Phaser.Scale.FIT,
        autoCenter:Phaser.Scale.CENTER_BOTH
    },
    
    backgroundColor:'#000000',
    
});
// @ts-ignore
game.scene.add(SCENE_KEYS.PRELOAD_SCENE, PreloadScene);
game.scene.add(SCENE_KEYS.GAME_SCENE, GameScen);
game.scene.add(SCENE_KEYS.GAME_OVER,GameOver);

