use windows::Win32::{
    Foundation::{HWND, LPARAM, LRESULT, WPARAM, RECT},
    Graphics::Gdi::ValidateRect,
    UI::WindowsAndMessaging::{
        CreateWindowExW, DefWindowProcW, DispatchMessageW, GetMessageW, LoadCursorW, PostQuitMessage,
        RegisterClassW, ShowWindow, TranslateMessage, CS_HREDRAW, CS_VREDRAW, CW_USEDEFAULT,
        IDC_ARROW, MSG, SW_SHOW, WM_DESTROY, WM_PAINT, WNDCLASSW, WS_OVERLAPPEDWINDOW,
    },
};
use windows::core::PCWSTR;

fn main() -> windows::core::Result<()> {
    let h_inst = windows::Wind32::System::LibraryLoader::GetModuleHandleW(None)?;
    let w_class = PCWSTR::from_wide(&[b'M' as u16, b'y' as u16, b'l' as u16, b'a' as u16, b's' as u16, b's' as u16, 0]);

    let app_window = WNDCLASSW {
        hCursor: unsafe { LoadCursorW(None, IDC_ARROW) },
        hInstance: h_inst,
        lpszClassName: w_class,
        style: CS_HREDRAW | CS_VREDRAW,
        lpfnWndProc: Some(window_proc),
        ..Default::default()
    };
    unsafe { RegisterClassW(&window_class) };
    let hwnd = unsafe {
        CreateWindowExW(
            Default::default(),
            w_class,
            PCWSTR::from_wide(&[b'M' as u16, b'y' as u16, b' ' as u16, b'W' as u16, b'i' as u16, b'n' as u16, b'd' as u16, b'o' as u16, b'w' as u16, 0]),
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            None,
            None,
            h_inst,
            std::ptr::null_mut(),
        )
    };
    unsafe { ShowWindow(hwnd, SW_SHOW) };
    let mut msg = MSG::default();
    while unsafe { GetMessageW(&mut msg, None, 0, 0) }.into() {
        unsafe {
            TranslateMessage(&msg);
            DispatchMessageW(&msg);
        }
    }
    Ok(())
}

extern "system" fn window_proc(hwnd: HWND, msg: u32, w_param: WPARAM, l_param: LPARAM) -> LRESULT {
    match msg {
        WM_PAINT => {
            unsafe { ValidateRect(hwnd, std:ptr::null()) };
            LRESULT(0)
        }
        WM_DESTROY => {
            unsafe { PostQuitMessage(0) };
            LRESULT(0)
        }
        _ => unsafe { DefWindowProcW(hwnd, msg, w_param, l_param) },
    }
}