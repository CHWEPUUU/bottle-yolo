import gradio as gr
import torch
import glob

# model = torch.hub.load("0_yolov7","custom", path_or_model="/home/zyzmu/yolov7-Improve/0_yolov7/runs/train/yolov7-tiny_bottle-sg4/weights/best.pt", source="local")  # or yolov5n - yolov5x6, custom

base_path = 'F:/Code/Code_Vue/yolo/yolov7/'

def getFileName(chos):
    file_names = glob.glob("F:/Code/Code_Vue/yolo" + "/*")
    file_names = [f.split('/')[-1] for f in file_names if '.' not in f]
    file_names.sort()
    for file_name in file_names:
        if chos.split('-')[-1] in file_name:
            return file_name

def detect(img, chos, Image_Size, Confidence_threshold, IoU_threshold):
    model = torch.hub.load(getFileName(chos), "custom", path_or_model=base_path + chos + '.pt', source="local")
    model.imgsz = Image_Size
    model.conf = Confidence_threshold
    model.iou = IoU_threshold
    
    return model(img).render()[0]


demo = gr.Interface(fn=detect, 
                    inputs=[gr.Image(height=640, width=1024),
                            gr.Dropdown(["yolov7-tiny", 
                                        "yolov7-tiny-wiou", 
                                        "yolov7-tiny-gold",
                                        ], label="Model", value="yolov7-tiny-gold"),
                            gr.Dropdown([640, 320], label="Image Size", value=640),
                            gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
                            gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold")
                            ],         
                    outputs=[gr.Image(height=640, width=1024)],
                    title='基于Gradio的yolov7改进液位检测应用',
                    # examples=[['/home/zyzmu/data/bottle_VOC2007/images/val/6E1ADCCBF70C880015C1F30504DDD672.jpg'],
                    #           ['/home/zyzmu/data/bottle_VOC2007/images/val/A0708A3D855569503CB87564E3EC035F.jpg'],
                    #           ['/home/zyzmu/data/bottle_VOC2007/images/val/A46E2F0C8C20353FA0433AF78FBB4710.jpg']]
                    )
    
if __name__ == "__main__":
    demo.launch(show_api=False)