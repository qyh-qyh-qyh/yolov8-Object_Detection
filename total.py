import queue
import threading
import cv2
from ultralytics import YOLO
import RPi.GPIO as GPIO
import time

# 设置GPIO引脚编号模式
GPIO.setmode(GPIO.BCM)

# 定义电机引脚
motor_pins = [18, 23, 24, 25]
break_pins = [22, 27]

# 设置引脚为输出
for pin in motor_pins + break_pins:
    GPIO.setup(pin, GPIO.OUT)

# 设置PWM频率
pwm_freq = 100

# 创建PWM对象
pwms = [GPIO.PWM(pin, pwm_freq) for pin in motor_pins]

# 创建一个消息队列
message_queue = queue.Queue()


def set_speed():
    while True:
        speed = input("请输入期望的转速（0-100）: ")
        try:
            speed = float(speed)
            if 0 <= speed <= 100:
                return speed
            else:
                print("转速必须在0到100之间")
        except ValueError:
            print("请输入有效的数字")


def start_motors(desired_speed):
    for pwm in pwms:
        pwm.start(desired_speed)
    print("电机启动")


def stop_motors():
    for pwm in pwms:
        pwm.ChangeDutyCycle(0)

    for pin in motor_pins:
        GPIO.output(pin, GPIO.LOW)

    time.sleep(1)  # 等待电机完全停止
    print("电机刹车")


def detect_target(results):
    for result in results:
        if result.prediction == 2:  # 检测到黑点
            return True
    return False


def visual_processing():
    model = YOLO('stem_and_black_spot.pt')  # 加载YOLOv8模型

    address = "udp://localhost:5000"
    cap = cv2.VideoCapture(address)  # 0表示默认摄像头，如果有多个摄像头，可以尝试使用1, 2, 等

    while cap.isOpened():
        success, frame = cap.read()
        if success:
            results = model(frame)
            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8推理", annotated_frame)

            if detect_target(results):
                message_queue.put("STOP")
            else:
                message_queue.put("GO")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    message_queue.put(None)
    cap.release()
    cv2.destroyAllWindows()


def mobile_processing():
    #start_motors(10)
    while True:
        message = message_queue.get()
        if message == "STOP":
            stop_motors()  # 停止移动
            time.sleep(5)#默认给5秒进行喷洒
        elif message == "GO":
            start_motors(10)
        elif message is None:
            break





# 创建视觉处理线程
visual_thread = threading.Thread(target=visual_processing)
visual_thread.start()

# 创建移动处理线程
mobile_thread = threading.Thread(target=mobile_processing)
mobile_thread.start()

# 等待视觉处理线程完成
visual_thread.join()
mobile_thread.join()

# 捕获键盘中断信号，停止PWM
#stop_motors()
GPIO.cleanup()
