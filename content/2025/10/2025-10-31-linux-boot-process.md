---
title: "Linux Boot Process"
date: 2025-10-31
type: diagram
tags:
  - linux
  - boot-process
  - os
---

### High-Level Overview of the Boot Process

```mermaid
graph TD
    subgraph Hardware
        A[Power On] --> B[CPU Reset];
    end

    subgraph Firmware
        B --> C[Firmware Execution <br/>BIOS/UEFI];
        C --> D[POST <br/>Power-On Self-Test];
        D --> E[Locate Boot Device];
    end

    subgraph Bootloader
        E --> F[Load Bootloader];
        F --> G[Bootloader Executes];
        G --> H[Load Kernel & Initrd];
    end

    subgraph Early Kernel
        H --> I[CPU Mode Switch <br/>Real -> Protected -> Long];
        I --> J[Unpack Kernel];
        J --> K[Jump to Kernel Entry Point];
    end

    subgraph Main Kernel
        K --> L[start_kernel function runs];
    end

    style A fill:#e6e6ff,stroke:#333,stroke-width:2px
    style B fill:#e6e6ff,stroke:#333,stroke-width:2px
    style C fill:#e6e6ff,stroke:#333,stroke-width:2px
    style D fill:#e6e6ff,stroke:#333,stroke-width:2px
    style E fill:#e6e6ff,stroke:#333,stroke-width:2px
    style F fill:#e6e6ff,stroke:#333,stroke-width:2px
    style G fill:#e6e6ff,stroke:#333,stroke-width:2px
    style H fill:#e6e6ff,stroke:#333,stroke-width:2px
    style I fill:#e6e6ff,stroke:#333,stroke-width:2px
    style J fill:#e6e6ff,stroke:#333,stroke-width:2px
    style K fill:#e6e6ff,stroke:#333,stroke-width:2px
    style L fill:#e6e6ff,stroke:#333,stroke-width:2px
```

### Firmware Hand-off: BIOS vs. UEFI

```mermaid
graph TD
    subgraph CPU Starts
        A[CPU Jumps to Reset Vector at 0xFFFFFFF0] --> B[Firmware Code Begins];
    end

    B --> C{Select Boot Path};

    subgraph "BIOS (Legacy)"
        C -- Old Style --> D[Scan Boot Order];
        D --> E{Find Disk with Boot Signature <br/>0x55AA at end of first sector};
        E --> F[Copy first 512 bytes to 0x7C00];
        F --> G[Jump to 0x7C00 to run Bootloader];
    end

    subgraph "UEFI (Modern)"
        C -- New Style --> H[Read Filesystem from EFI System Partition];
        H --> I[Locate and Load Bootloader EFI file];
        I --> J[Execute Bootloader Program];
    end

    G --> K((Bootloader Takes Control));
    J --> K;
```

### CPU Mode Transition Sequence

```mermaid
sequenceDiagram
    participant RM as Real Mode Setup
    participant PM as Protected Mode (32-bit)
    participant LM as Long Mode (64-bit)

    Note over RM: CPU starts here. Addressing:<br/>(segment << 4) + offset
    RM->>RM: 1. Disable maskable interrupts
    RM->>RM: 2. Open A20 line to access >1MB RAM
    RM->>RM: 3. Load minimal GDT (Global Descriptor Table)
    RM->>RM: 4. Set PE bit in CR0 register
    RM->>PM: 5. Perform far jump to enter Protected Mode

    Note over PM: Now in 32-bit mode. Flat memory model.
    PM->>PM: 6. Build initial page tables (identity map)
    PM->>PM: 7. Enable PAE in CR4 register
    PM->>PM: 8. Load page table address into CR3
    PM->>PM: 9. Set LME bit in EFER register to allow Long Mode
    PM->>LM: 10. Perform far return to 64-bit code segment

    Note over LM: Now in 64-bit mode. Paging is active.
```

### Kernel Unpacking and Execution

```mermaid
graph TD
    A[64-bit Stub Starts] --> B{Handle kASLR?};
    B -- Yes --> C[Find Random Physical &<br/>Virtual Addresses];
    B -- No --> D[Use Default Addresses];
    C --> E[Clear BSS & Prepare<br/>Minimal Page Tables];
    D --> E;
    E --> F;

    subgraph Decompression
        F[Call extract_kernel C function] --> G[Print 'Decompressing<br/>Linux...'];
        G --> H[Unpack Kernel using<br/>chosen algorithm<br>gzip, zstd, etc.];
        H --> I[Parse ELF Headers];
        I --> J[Copy Kernel Segments to<br/>Final Location];
        J --> K{Apply Relocations if needed};
    end

    K --> L[Get Kernel Entry Point<br/>Address];
    L --> M[Jump to start_kernel,<br/>passing boot parameters];
```

### Kernel Address Space Layout Randomization (kASLR) Logic

```mermaid
graph TD
    A{kASLR Enabled?} -- No --> I[Use default addresses];
    A -- Yes --> C[Build 'Do Not Touch'<br/>Memory List];
    C --> D[Scan Firmware Memory Map<br/>for Large Free Regions];
    D --> E[Calculate Total Number of<br/>Available 'Slots' for the Kernel];
    E --> F[Get Random Number from<br/>Hardware Source];
    F --> G[Pick a Slot based on the<br/>Random Number];
    G --> H{Found a suitable slot?};
    H -- Yes --> J[Set Physical and Virtual<br/>Bases to Random Slot];
    H -- No --> K[Fallback to Default<br/>Addresses and Warn];
    I --> L((Continue Boot));
    J --> L;
    K --> L;
```
