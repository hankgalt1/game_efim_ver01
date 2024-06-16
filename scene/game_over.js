// @ts-ignore
import phaser from '../phaser.js';
import { SCENE_KEYS } from '../scene-keys.js';
import { GameScen } from './game_scene.js';

export class GameOver extends Phaser.Scene{
    constructor(){
        super({
            // @ts-ignore
            key:SCENE_KEYS.GAME_OVER,
            
        });
        console.log('Загрузочная сцена');
    }
//Функция для переменных загрузочного экрана.  
    init(data){console.log('init.gm')
    this.screenCenterX = this.cameras.main.worldView.x + this.cameras.main.width / 2;
    this.screenCenterY = this.cameras.main.worldView.y + this.cameras.main.height / 2;
    this.gold = data.score
    this.derevo_score = data.score1
    console.log(this.gold)
    console.log(this.derevo)
    

}
    
//Функция для загрузки ресурсов для загрузочного экрана.
    preload(){ 
        console.log('init.preload')
        this.load.image('start',`./game_window/start.png`)}
//Функция для создания на кэнвасе объектов загрузочного экрана.
    create(){console.log('init.create')
    this.add.image(-4,-4,'bg').setOrigin(0).setDisplaySize(this.scale.width+4,this.scale.height+4)
    this.moneta = this.add.image(this.scale.width/3.5,this.scale.height/1.5,'moneta').setDisplaySize(this.scale.width/3,this.scale.width/3)
    this.derevo =this.add.image(this.scale.width/1.5,this.scale.height/1.5,'derevo').setDisplaySize(this.scale.width/3,this.scale.width/3)
    this.Name_Preload_text =this.add.text(this.screenCenterX,this.scale.height/3, 'GAME OVER', {
        font: `600 ${this.scale.width/6}px font1`,
        color:'#000000' 
    }).setOrigin(0.5)
    this.Name_gold =this.add.text(this.moneta.x,this.scale.height-this.derevo.y/4,`${this.gold}`, {
        font: `600 ${this.scale.width/8}px font1`,
        color:'#000000' 
    }).setOrigin(0.5)
    this.Name_derevo =this.add.text(this.derevo.x,this.scale.height-this.derevo.y/4,`${this.derevo_score}`, {
        font: `600 ${this.scale.width/8}px font1`,
        color:'#000000' 
    }).setOrigin(0.5)
    
    //this.add.image(this.screenCenterX,this.scale.height/1.1,'start').setDisplaySize(this.scale.width/2,this.scale.height/10).setInteractive().on('pointerdown', () =>  this.scene.start(SCENE_KEYS.GAME_SCENE, GameScen));

}
//Функция для обновления данных загрузочного экрана.
    update(){console.log('init.update')} 
}
