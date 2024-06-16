// @ts-ignore
import phaser from '../phaser.js';
import { SCENE_KEYS } from '../scene-keys.js';


export class GameOver extends Phaser.Scene{
    constructor(){
        super({
            // @ts-ignore
            key:SCENE_KEYS.GAME_OVER,
            
        });
        console.log('Загрузочная сцена');
    }
//Функция для переменных загрузочного экрана.  
    init(){console.log('init.gm')
    this.screenCenterX = this.cameras.main.worldView.x + this.cameras.main.width / 2;
    this.screenCenterY = this.cameras.main.worldView.y + this.cameras.main.height / 2;}
    
//Функция для загрузки ресурсов для загрузочного экрана.
    preload(){ 
        console.log('init.preload')}
//Функция для создания на кэнвасе объектов загрузочного экрана.
    create(){console.log('init.create')
    this.Name_Preload_text =this.add.text(this.screenCenterX,this.scale.height/2, 'GAME_OVER', {
        font: `600 ${this.scale.width/6}px font1`,
        color:'#ffffff' 
    }).setOrigin(0.5)}
//Функция для обновления данных загрузочного экрана.
    update(){console.log('init.update')} 
}
