from fastapi import FastAPI, Form, File
from fastapi.responses import FileResponse
import cairosvg
import io

app = FastAPI()

@app.post('/generate_image/')
async def generate_image(text: str = Form(...)):
    try:
        # SVGテンプレート
        svg_template = f'<svg width="400" height="200"><text x="10" y="50" font-family="Arial" font-size="20">{text}</text></svg>'

        # SVGをPNGに変換
        png_data = cairosvg.svg2png(bytestring=svg_template.encode('utf-8'))

        # PNGデータをファイルライクなオブジェクトに変換
        png_io = io.BytesIO(png_data)

        # ファイルライクなオブジェクトを送信
        return FileResponse(png_io, media_type='image/png')

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)